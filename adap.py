import asyncio
import time
from DBAccess.DBBridge import dbbridge

class STFF_Adapter:
    """This module provides access to database for working with halfstuff"""

    def __init__(self):
        """Creates DBBridge element for working with db"""
        self.bridge = dbbridge.DBBridge()

    async def update_Renew_Reservation(self, adapterData):
        """FN_RenewReservation functon call
        Parameters:
        adapterData : list of parameters for db function:
            Parameters for db function:
            Cell code where halfstuff have to be reserved from : string
            The number of hulfstuff units which are taken for a dish : int
            Is balance reset required : bool
        Returns:
        bool
            If function successful
        """
        print(time.time())
        try:
            function_result = self.bridge.execute_db_proc_with_params('FN_RenewReservation', adapterData)
            is_function_successful = function_result[0][0]
        except:
            print('Three parameters are required')
            is_function_successful = False
        finally:
            print(time.time())
            return is_function_successful


    def select_DefineSTFFCell(self, adapterData):
        """FN_DefineSTFFCell function call
        Parameters:
        adapterData : list of parameters for db function:
            Parameters for db function:
            Halfstuff ID of the product which are going to be used in a dish : string (uuid in db)
        Returns:
        list of (string, int)
            Defined codes of fridge doors where are required halfstuff,
            The code of particular product in a cell
        """
        print(time.time())
        try:
            function_result = self.bridge.execute_db_proc_with_params('FN_DefineSTFFCell', adapterData)
            defined_cells = function_result[0][0]
        except:
            print('Two parameters are required')
            defined_cells = None
        finally:
            print(time.time())
            return defined_cells
