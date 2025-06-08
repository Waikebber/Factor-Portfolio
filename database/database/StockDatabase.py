import sqlite3
import os
import time
from datetime import datetime, timedelta
from typing import List, Optional
from tqdm import tqdm
import sys
from pathlib import Path
import pandas as pd

sys.path.append(str(Path(__file__).parent.parent.parent))
from .db_writers import *

class StockDatabase:
    def __init__(self, db_name='../stock_data.db'):
        self.db_name = db_name
        self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), db_name)

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def initialize(self):
        try:
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            conn = self._get_connection()
            cursor = conn.cursor()

            # Initialize schema/execute sql files
            schema_dir = os.path.join(os.path.dirname(__file__), "schema")
            schema_dirs = [
                'core',           # Core tables first
                'market_data',    # Market data tables
                'financial_metrics', # Financial metrics
                'valuation',      # Valuation tables
                'analyst_data',   # Analyst data
                'corporate_actions', # Corporate actions
                'macro',          # Macro data
                'analysis',       # Analysis tables
                'growth'          # Growth tables
            ]
            with tqdm(total=len(schema_dirs), desc="Initializing database schema", unit="dir") as pbar:
                for dir_name in schema_dirs:
                    dir_path = os.path.join(schema_dir, dir_name)
                    if os.path.exists(dir_path):
                        sql_files = [f for f in os.listdir(dir_path) if f.endswith('.sql')]
                        sql_files.sort()
                        for sql_file in sql_files:
                            file_path = os.path.join(dir_path, sql_file)
                            with open(file_path, 'r') as f:
                                cursor.executescript(f.read())
                    pbar.update(1)
            
            conn.commit()
            conn.close()
            print("Database initialization complete.")
        except Exception as e:
            print(f"Failed to initialize database: {str(e)}")
            return False

    def delete(self):
        try:
            if os.path.exists(self.db_path):
                os.remove(self.db_path)
            return True
        except Exception as e:
            print(f"Error deleting database: {e}")
            return False
    
    def export_to_excel(self, file_path: str):
        """Export all tables in the database to an Excel file, one sheet per table.
        
        Args:
            file_path (str): Path to save the Excel file (e.g., "output.xlsx")
        """
        try:
            conn = self._get_connection()
            cursor = conn.cursor()
            
            # Get all user-defined tables
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
            tables = [row[0] for row in cursor.fetchall()]
            
            if not tables:
                print("No tables found in the database.")
                return
            
            with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
                for table in tables:
                    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)
                    df.to_excel(writer, sheet_name=table[:31], index=False)  # Sheet name max length is 31
            
            print(f"Export complete: {file_path}")
            conn.close()
        except Exception as e:
            print(f"Failed to export database to Excel: {e}")

if __name__ == "__main__":
    db = StockDatabase()
    db.initialize()
