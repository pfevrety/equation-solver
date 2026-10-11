# Equation solver

A small Python expression parser and polynomial simplifier. It reads an expression, parses it into an abstract syntax tree (AST), evaluates that tree, and prints the simplified result in the terminal.

```text
$ python main.py "2x + 5x + 2 - 29 + xxx + 3t"
-27 + 7x + x^3 + 3t
```

## How it works

The expression passes through three stages:

1. **Lexer** (`lexer.py`) converts the input text into tokens such as numbers, operators, variables, parentheses, and function names. It also recognizes implicit multiplication, so `2x` and `2(x + 1)` are accepted.
2. **Parser** (`parser_.py`) applies operator precedence and builds an AST from the tokens. For example, `2 + 3 * x` becomes an addition node whose right child is a multiplication node.
3. **Interpreter** (`interpreter.py`) walks the AST, evaluates operations, combines like polynomial terms, and returns a printable result.

The AST node types are defined in `nodes.py`. This separation makes it possible to extend the syntax or add new operations without putting all parsing and evaluation logic in one place.

## Features

- Addition, subtraction, multiplication, and division by a non-zero constant.
- Parentheses and standard arithmetic precedence.
- Implicit multiplication, for example `2x`, `xy`, and `3(x + 1)`.
- Polynomial term collection, including powers such as `x^2` (written as `xx`).
- Numeric constants `π`, `e`.
- Numeric functions: `sin`, `cos`, `tan`, `sqrt`, `log` (natural logarithm), `ln`, `exp`, and `abs`.

Function calls use parentheses. Numeric arguments are evaluated directly; symbolic arguments are kept as function terms and can be differentiated:

```bash
python main.py "sin(π / 2) + sqrt(9)"
```

Use `π` for pi; the word `pi` is currently parsed as variables. Trigonometric functions use radians.

## Usage

Python 3.9 or newer is required. There are no external dependencies.

Pass an expression on the command line:

```bash
python main.py "(x + 2) * 3 - x"
```

Or run without an argument to enter one interactively:

```text
$ python main.py
expression> 2x + 3x
5x
```

The simplifier can also be imported:

```python
from main import simplify

print(simplify("2x + 3x"))  # 5x
```

Differentiate with `--derive`, and add `--steps` to print intermediate reductions:

```bash
python main.py --derive x "xx + sin(x)"
python main.py --steps "(x + 1)(x + 2)"
```

## Scope

This is an expression simplifier, not an equation solver: it does not solve equalities or inequalities. Symbolic functions are preserved and can be differentiated with the chain rule. Division supports constants and single monomials, not general rational expressions. Derivatives are supported for `sin`, `cos`, `tan`, `exp`, `log`/`ln`, and `sqrt`; `abs` remains numeric only.
