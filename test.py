"""Test cases:

@@Test Case 1: Check count for [Person].[Address]
@@Test Case 2: Check count for [Production].[Document]
@@Test Case 3: Check count for [Production].[UnitMeasure]
@@Test Case 4: Check uniqueness of the value in [Person].[Address].[AddressID]
@@Test Case 5: Check uniqueness of the value in [Production].[Document].[DocumentID]
@@Test Case 6: Check uniqueness of the value in [Production].[UnitMeasure].[UnitMeasureCode]
@@Test Case 7: Check null values in [Person].[Address]
@@Test Case 8: Check null values in [Production].[Document]
@@Test Case 9: Check null values in [Production].[UnitMeasure]"""

# import dqe_mentoring.app
from app import CURSOR


# Test Case 1: Check count for [Person].[Address]
def test_count_person_address():
    query_string = f'SELECT COUNT(*) FROM [AdventureWorks2012].[Person].[Address]'
    assert CURSOR.execute(query_string).fetchval() == 3


# Test Case 2: Check count for [Production].[Document]
def test_count_production_document():
    query_string = f'SELECT COUNT(*) FROM [AdventureWorks2012].[Production].[UnitMeasure]'
    assert CURSOR.execute(query_string).fetchval() == 3


# Test Case 3: Check count for [Production].[UnitMeasure]
def test_count_production_unit_measure():
    query_string = f'SELECT COUNT(*) FROM [AdventureWorks2012].[Production].[Document]'
    assert CURSOR.execute(query_string).fetchval() == 3


# Test Case 4: Check uniqueness of the value in [Person].[Address].[AddressID]
def test_uniqueness_person_address_address_id():
    query_string = f'SELECT Person.Address.AddressID, COUNT(AddressID) as \'Count\' ' \
                   f'FROM [AdventureWorks2012].[Person].[Address] GROUP BY AddressID HAVING COUNT(AddressID) > 1 '
    assert CURSOR.execute(query_string).fetchval() is None


# Test Case 5: Check uniqueness of the value in [Production].[Document].[DocumentID]
def test_uniqueness_production_document_document_id():
    query_string = f'      SELECT [Production].[Document].[DocumentID], COUNT([DocumentID]) as \'Count\' ' \
                   f'      FROM  [AdventureWorks2012].[Production].[Document] GROUP BY [DocumentID] ' \
                   f'      HAVING COUNT([DocumentID]) > 1 '
    assert CURSOR.execute(query_string).fetchval() is None


# Test Case 6: Check uniqueness of the value in [Production].[UnitMeasure].[UnitMeasureCode]
def test_uniqueness_production_unit_measure_unit_measure_code():
    query_string = f'    SELECT [Production].[UnitMeasure].[UnitMeasureCode], COUNT([UnitMeasureCode]) as \'Count\' ' \
                   f' FROM [AdventureWorks2012].[Production].[UnitMeasure] GROUP BY [UnitMeasureCode] ' \
                   f' HAVING COUNT([UnitMeasureCode]) > 1'
    assert CURSOR.execute(query_string).fetchval() is None


# Test Case 7: Check null values in [Person].[Address]
def test_null_person_address():
    query_string = f'    SELECT [UnitMeasureCode] ' \
                   f'	 FROM [AdventureWorks2012].[Production].[UnitMeasure] ' \
                   f'    WHERE [UnitMeasureCode] is null '
    assert CURSOR.execute(query_string).fetchval() is None


# Test Case 8: Check null values in [Production].[Document]
def test_null_production_document():
    query_string = f' SELECT [DocumentNumber] from [AdventureWorks2012].[Production].[Document] ' \
                   f' WHERE [DocumentNumber] IS NULL '
    assert CURSOR.execute(query_string).fetchval() is None


# Test Case 9: Check null values in [Production].[UnitMeasure]
def test_null_production_unit_measure():
    query_string = f'    SELECT [UnitMeasureCode] ' \
                   f'	 FROM [AdventureWorks2012].[Production].[UnitMeasure] ' \
                   f'    WHERE [UnitMeasureCode] is null '
    assert CURSOR.execute(query_string).fetchval() is None
