# CLAUDE.md — Calculadora Multifuncional

This file describes the structure, conventions, and development workflows for this project, intended as a reference for AI assistants and developers.

---

## Project Overview

A multi-function desktop calculator built in **Python** with **PySide6 (Qt6)**. The application provides a standard arithmetic calculator plus several unit/value converters, all within a single-window interface navigated via a hamburger menu.

The project is developed for Windows and distributed as a standalone `.exe` via PyInstaller.

---

## Repository Structure

```
calculadora-teste/
├── Calculadora/                  # All application source files
│   ├── calculadora.py            # Main application logic (entry point)
│   ├── calculadora_ui.py         # Auto-generated UI class from Qt Designer (DO NOT edit manually)
│   ├── calculadora.ui            # Qt Designer XML layout file (edit in Qt Designer)
│   ├── calculadora.spec          # PyInstaller build specification
│   ├── dist/
│   │   └── calculadora.exe       # Pre-built Windows executable
│   ├── build/                    # PyInstaller intermediate build artefacts
│   ├── DS-DIGIT.ttf              # Custom 7-segment display font (main)
│   ├── DS-DIGII.ttf              # Custom 7-segment display font (variant)
│   ├── DS-DIGIB.ttf              # Custom 7-segment display font (bold)
│   ├── DS-DIGI.ttf               # Custom 7-segment display font (regular)
│   ├── icon.ico                  # Application icon
│   ├── arrow.png                 # Custom dropdown arrow for QComboBox
│   ├── calendar.png              # Custom calendar icon for QDateEdit
│   ├── construcao.png            # "Under construction" placeholder image
│   ├── down.png                  # Arrow image
│   ├── icons/                    # Alternative icon versions
│   ├── calculadora.old.ui        # Legacy Qt Designer file (archived)
│   ├── calculadora_ui.old.py     # Legacy generated UI (archived)
│   ├── calculadora.old_ui.py     # Legacy generated UI (archived)
│   ├── calculadora-backup.py     # Backup of main logic
│   ├── calculadora cod limpo.py  # Cleaned-up code draft
│   ├── calculadora com lcd.py    # Experimental LCD-style variant
│   └── comandos .md              # Developer notes: CSS snippets and Qt style references
├── Comandos venv pyside 6.txt    # Notes for setting up the virtual environment
├── README.md                     # Minimal project readme
└── __pycache__/                  # Python bytecode cache (CPython 3.14)
```

---

## Technology Stack

| Component        | Technology                          |
|-----------------|--------------------------------------|
| Language         | Python 3.14                         |
| UI Framework     | PySide6 6.10.2 (Qt6)               |
| UI Design        | Qt Designer (`.ui` files)           |
| HTTP Requests    | `requests`                          |
| Date Arithmetic  | `python-dateutil` (`relativedelta`) |
| Build/Packaging  | PyInstaller                         |
| Target Platform  | Windows (`.exe`)                    |

---

## Application Architecture

### Entry Point

`Calculadora/calculadora.py` is the application entry point. It:
1. Creates the `QApplication` and `QDialog` window
2. Instantiates and sets up the generated `Ui_Dialog` class from `calculadora_ui.py`
3. Applies all styles (inline Python QSS)
4. Defines all business logic functions at module level
5. Connects all Qt signals to functions
6. Calls `janela.show()` and `app.exec()` to launch

### UI Layer

`calculadora_ui.py` is **auto-generated** by Qt's `pyside6-uic` tool from `calculadora.ui`. It must **never be edited manually** — changes will be overwritten on next UI compilation.

The UI is structured as a `QStackedWidget` with multiple pages (indexes):

| Index | Page Name              | Description                                  |
|-------|------------------------|----------------------------------------------|
| 0     | `calculadora`          | Standard arithmetic calculator               |
| 1     | Distâncias             | Distance unit converter                      |
| 2     | Temperatura            | Temperature unit converter                   |
| 3     | Tempo                  | Time unit converter                          |
| 4     | Datas (diff)           | Date difference calculator                   |
| 5     | Datas (arithmetic)     | Add/subtract days/months/years from a date   |
| 6     | Velocidades            | Speed converter (under construction)         |
| 7     | Moedas                 | Currency converter                           |

Navigation between pages is done via a `QMenu` triggered by any `toolButton_N` (hamburger menu buttons, one per page).

### State Management

Calculator state is managed with **module-level global variables**:

```python
valor_atual        # The first operand stored after pressing an operator
operador           # Current pending operator: "+", "-", "*", "/"
resultado          # Last computed result
resultado_mostrado # True when display shows a result (affects next digit input)
segundo_valor      # The second operand (in-progress)
texto_atual        # Current text shown on display
convertendo        # Mutex flag — prevents recursive converter loops
ajustando_texto    # Mutex flag — prevents recursive text-substitution loops
menu               # Reference to the active QMenu
```

---

## Key Conventions

### Language

All variable names, function names, and UI widget names are in **Portuguese** (European Portuguese). Examples:
- `janela` = window
- `resultado` = result / equals
- `valor_atual` = current value
- `operador` = operator
- `limpar_tudo` = clear all (AC button)
- `apagar` = backspace
- `decimal` = decimal point
- `sinal` = sign toggle (+/-)
- `convertendo` = converting (mutex)

### Decimal Separator

The application uses **comma (`,`) as the decimal separator** (Portuguese standard). Input fields use a `QDoubleValidator` configured with `QLocale(QLocale.Portuguese, QLocale.Portugal)`. The `FiltroVirgula` event filter class intercepts period key presses and converts them to commas to handle keyboards that produce `.` for the decimal key.

### Number Formatting (`formatar_numero`)

Results in conversion pages are formatted by `formatar_numero()`:
- Rounds to 4 decimal places
- Uses space as the thousands separator
- Uses comma as decimal separator
- Strips trailing zeros

### Conversion Architecture

Each converter (distance, temperature, time) uses:
1. A **dictionary** mapping unit names to a base-unit multiplier (or tuple for non-linear conversions like temperature)
2. Two symmetric functions (`converter_X1`, `converter_X2`) — one for each input field — that convert in opposite directions
3. The `convertendo` flag prevents infinite recursion when updating the opposite field triggers `textChanged`

**Distance**: converts via metres as the base unit.
**Temperature**: converts to/from Celsius as the base unit using `(value, offset)` tuples.
**Time**: converts via hours as the base unit.

### Currency Converter

Fetches live exchange rates at startup from `exchangerate-api.com` using a hardcoded API key. The base currency is EUR. Rates are loaded once and stored in the `dados` response object. Combo boxes are pre-populated with ~70 named currencies.

> **Note**: The API key (`API_KEY`) is hardcoded in `calculadora.py:1046`. Treat it as a secret; do not commit changes that expose or rotate it carelessly.

### Asset Loading (`resource_path`)

```python
def resource_path(path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, path)
    return os.path.join(os.path.abspath("."), path)
```

All asset references (fonts, images, icons) must use `resource_path()` to be compatible with both the development environment and the PyInstaller-packaged `.exe`.

### Keyboard Shortcuts

The standard calculator page has `QShortcut` bindings for:
- Digits `0–9`, operators `+`, `-`, `/`, `*`
- `.` → decimal point
- `Backspace` → delete last character
- `Delete` → clear all

---

## Development Workflow

### Running the Application

```bash
cd Calculadora
python calculadora.py
```

The working directory must be `Calculadora/` because assets (fonts, images, icon) are referenced relative to that directory.

### Setting Up the Virtual Environment (PySide6)

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# or
source venv/bin/activate       # Linux/macOS

pip install PySide6 requests python-dateutil
```

### Editing the UI

1. Open `Calculadora/calculadora.ui` in **Qt Designer**
2. Make layout changes
3. Regenerate `calculadora_ui.py`:
   ```bash
   pyside6-uic calculadora.ui -o calculadora_ui.py
   ```
4. **Never** manually edit `calculadora_ui.py`

### Building the Executable

```bash
cd Calculadora
pyinstaller calculadora.spec
```

The output `.exe` will be at `Calculadora/dist/calculadora.exe`.

The `.spec` file includes these bundled data files:
- `icon.ico`
- `DS-Digit.ttf`
- `arrow.png`
- `calendar.png`
- `construcao.png`

If new assets are added, they must also be added to the `datas` list in `calculadora.spec`.

---

## Styling Conventions

All styles are applied programmatically in `calculadora.py` using inline QSS (Qt Style Sheets). The design language is:

- **Background**: `#f0f0f0` (light grey)
- **Buttons/inputs**: white background, `#333` text, `#ddd` border, `8px` border-radius
- **Accent/selection**: `#ff7052` / `#ff8c42` / `#ff5032` (orange-red gradient family)
- **Hover**: slightly darker grey (`#f5f5f5`) or orange accent
- **Font size**: 20px for calculator buttons, 11px for combo boxes
- **Display font**: DS-DIGIT.ttf at 72px, right-aligned

Each `QComboBox` requires styling both the widget itself (`setStyleSheet`) and its dropdown popup view (`.view().setStyleSheet()` and `.view().window().setStyleSheet()`).

---

## File Notes

- `calculadora.old.ui`, `calculadora_ui.old.py`, `calculadora.old_ui.py` — archived legacy versions; can be ignored
- `calculadora-backup.py`, `calculadora cod limpo.py`, `calculadora com lcd.py` — experimental/backup files; not part of the active codebase
- `comandos .md` — developer snippet reference for QSS styles (not executable code)
- `build/` — PyInstaller intermediate output; not committed or needed for development
- `__pycache__/` — Python bytecode; ignore

---

## Known Limitations / TODOs

- **Velocidades (Speed)** page is not yet implemented (shows a "under construction" image via `label_2`)
- **Definições (Settings)** and **Acerca de (About)** menu items both route to `stackedWidget` index 5, which appears to be a placeholder
- Currency API key is hardcoded — should be moved to a config file or environment variable for production use
- Extensive `print()` debug statements remain throughout `calculadora.py` (left from development)
- No automated tests exist
- The `apagar_tudo_foco` function only clears distance and temperature fields, not time fields
