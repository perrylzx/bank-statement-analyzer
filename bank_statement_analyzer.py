import dearpygui.dearpygui as dpg
import pandas as pd

statement = pd.read_csv('statement.csv')


def parseStatementToTableFormat():
    flattenedStatement = []
    for row in statement.itertuples(name=None):
        flattenedStatement.append(list(row))
    return flattenedStatement


def renderGUI():
    dpg.create_context()

    with dpg.window():
        with dpg.table(header_row=True, policy=dpg.mvTable_SizingStretchProp, borders_outerH=True, borders_innerH=True, borders_outerV=True):
            statementHeaders = list(statement)
            for header in statementHeaders:
                dpg.add_table_column(label=header)

            # this function turns the dataframe into a flattened list, where each element is each row in the dataframe. this is because pygui uses iteration to create columns and rows
            flattenedStatement = parseStatementToTableFormat()
            for rowNum in range(len(flattenedStatement)):
                with dpg.table_row():
                    for data in flattenedStatement[rowNum]:
                        with dpg.table_cell():
                            dpg.add_text(f"{data}")

    dpg.create_viewport(title='Bank Statement Analyzer',
                        width=800, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


renderGUI()
