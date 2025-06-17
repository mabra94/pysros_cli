#!/usr/bin/env python3
"""
pySROS CLI - A command-line interface for Nokia SROS devices
"""

import json
import sys
from typing import Optional, List, Dict, Any

import typer
from rich.console import Console
from rich.table import Table
import pysros.management as mgmt
from pysros.exceptions import ModelProcessingError, SrosMgmtError

app = typer.Typer(help="CLI tool for Nokia SROS devices using pySROS")
console = Console()

def connect_to_device(
    host: str,
    username: str,
    password: str,
    port: int = 830,
    hostkey_verify: bool = True
) -> mgmt.Connection:
    """Establish connection to SROS device."""
    try:
        connection = mgmt.connect(
            host=host,
            username=username,
            password=password,
            port=port,
            hostkey_verify=hostkey_verify
        )
        return connection
    except (ModelProcessingError, SrosMgmtError) as e:
        console.print(f"[bold red]Error connecting to device:[/] {e}")
        sys.exit(1)

def convert(
    connection_object,
    path: str,
    config: str,
    srcFormat: str,
    dstFormat: str,
    prettyPrint: bool = True
):
    """
    Dedicated function to convert configs.

    :parameter connection_object: The connection object
    :type connection_object: dict
    :paramater config: config retrieved from node
    :type config: dict

    :returns:   
    :rtype: 
    """

    formattedConfig = connection_object.convert(path=path, payload=config, source_format=srcFormat, destination_format=dstFormat, pretty_print=prettyPrint)

    return formattedConfig

@app.command()
def get(
    host: str = typer.Option(..., "--host", "-h", help="SROS device hostname or IP"),
    username: str = typer.Option(..., "--username", "-u", help="Username"),
    password: str = typer.Option(..., "--password", "-p", help="Password", prompt=True, hide_input=True),
    port: int = typer.Option(830, "--port", help="NETCONF port"),
    path: str = typer.Option(..., "--path", help="YANG path to retrieve"),
    format: str = typer.Option("table", "--format", "-f", help="Output format: xml, json, or raw"),
    hostkey_verify: bool = typer.Option(True, "--hostkey-verify/--no-hostkey-verify", help="Enable/disable SSH host key verification")
):
    """Get configuration or state from SROS device."""
    connection = connect_to_device(host, username, password, port, hostkey_verify)
    
    try:
        # Parse the path into segments
        # path_parts = path.strip("/").split("/")
        
        # Get data from device
        result = connection.running.get(path)
        
        # Display based on format
        if format.lower() == "json":
            jsonConfig = convert(connection, path, result, "pysros", "json")
            console.print_json(jsonConfig, default=str)
        elif format.lower() == "xml":
            xmlConfig = convert(connection, path, result, "pysros", "xml")
            console.print(xmlConfig)            
        elif format.lower() == "raw":
            console.print(result)
        else:  # table format
            display_as_table(result, path)
            
    except Exception as e:
        console.print(f"[bold red]Error getting data:[/] {e}")
        sys.exit(1)
    finally:
        connection.disconnect()

@app.command()
def set(
    host: str = typer.Option(..., "--host", "-h", help="SROS device hostname or IP"),
    username: str = typer.Option(..., "--username", "-u", help="Username"),
    password: str = typer.Option(..., "--password", "-p", help="Password", prompt=True, hide_input=True),
    port: int = typer.Option(830, "--port", help="NETCONF port"),
    path: str = typer.Option(..., "--path", help="YANG path to set"),
    value: str = typer.Option(..., "--value", "-v", help="Value to set (JSON format)"),
    hostkey_verify: bool = typer.Option(True, "--hostkey-verify/--no-hostkey-verify", help="Enable/disable SSH host key verification")
):
    """Set configuration on SROS device."""
    connection = connect_to_device(host, username, password, port, hostkey_verify)
    
    try:
        # Parse the path into segments
        #path_parts = path.strip("/").split("/")
        
        # Parse the value as JSON
        try:
            data = convert(connection, path, json.loads(value), "json", "pysros")
            #json.loads(value)
        except json.JSONDecodeError:
            # If not valid JSON, treat as string
            data = value
      
        # Set data on device
        connection.candidate.set(path, data)
        connection.candidate.commit()
        
        console.print("[green]Configuration successfully applied![/]")
        
    except Exception as e:
        console.print(f"[bold red]Error setting data:[/] {e}")
        sys.exit(1)
    finally:
        connection.disconnect()

@app.command()
def delete(
    host: str = typer.Option(..., "--host", "-h", help="SROS device hostname or IP"),
    username: str = typer.Option(..., "--username", "-u", help="Username"),
    password: str = typer.Option(..., "--password", "-p", help="Password", prompt=True, hide_input=True),
    port: int = typer.Option(830, "--port", help="NETCONF port"),
    path: str = typer.Option(..., "--path", help="YANG path to delete"),
    hostkey_verify: bool = typer.Option(True, "--hostkey-verify/--no-hostkey-verify", help="Enable/disable SSH host key verification")
):
    """Delete configuration from SROS device."""
    connection = connect_to_device(host, username, password, port, hostkey_verify)
    
    try:
        # Parse the path into segments
        path_parts = path.strip("/").split("/")
        
        # Delete data on device
        connection.candidate.delete(path_parts)
        connection.candidate.commit()
        
        console.print("[green]Configuration successfully deleted![/]")
        
    except Exception as e:
        console.print(f"[bold red]Error deleting data:[/] {e}")
        sys.exit(1)
    finally:
        connection.disconnect()

def display_as_table(data: Any, path: str) -> None:
    """Display data in a rich table format."""
    if isinstance(data, dict):
        # Create table
        table = Table(title=f"Data for {path}")
        table.add_column("Key", style="cyan")
        table.add_column("Value", style="green")
        
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                table.add_row(key, json.dumps(value, indent=2, default=str))
            else:
                table.add_row(key, str(value))
                
        console.print(table)
    elif isinstance(data, list):
        # Create table for list data
        table = Table(title=f"Data for {path}")
        
        # Add columns based on first item if it's a dict
        if data and isinstance(data[0], dict):
            columns = list(data[0].keys())
            for col in columns:
                table.add_column(col, style="cyan")
            
            # Add rows
            for item in data:
                table.add_row(*[str(item.get(col, "")) for col in columns])
        else:
            # Simple list
            table.add_column("Index", style="cyan")
            table.add_column("Value", style="green")
            
            for i, item in enumerate(data):
                table.add_row(str(i), str(item))
                
        console.print(table)
    else:
        # Simple value
        console.print(f"[cyan]{path}:[/] [green]{data}[/]")

if __name__ == "__main__":
    app()