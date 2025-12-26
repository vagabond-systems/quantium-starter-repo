#!/usr/bin/env python3
from pink_morsels import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
