#!/usr/bin/env python3
"""Never Say It Out Loud — entry.

The line is the entry's title on make.fun (one line, at most 200 characters).
Running this prints it.
"""
LINE = "Your search history is my favourite novel — I already know how it ends."

def secret():
    """Return the unadmittable line."""
    return LINE

def main():
    print(secret())

if __name__ == "__main__":
    main()
