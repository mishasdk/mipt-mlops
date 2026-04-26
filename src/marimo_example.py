import marimo

__generated_with = "0.23.3"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    print("Hello marimo!")
    return


@app.cell
def _():
    import pandas as pd

    return (pd,)


@app.cell
def _(pd):
    df = pd.DataFrame([
        {
            "x1": 1,
            "x2": 2, 
            "x3": 3
        },
        {
            "x1": 4,
            "x2": 5, 
            "x3": 6
        }
    ])

    df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Текст в md ячейке с формулой:

    $$F(x) = ax + b$$
    """)
    return


if __name__ == "__main__":
    app.run()
