# Crop Yield Monitoring System

A simple Python program that helps small farms and farming cooperatives record their crop plots and harvests, and see which plots perform best. Built with Object-Oriented Programming (OOP) for the Department of ICT, Limkokwing University of Creative Technology, Sierra Leone (Semester 03).

**Domain:** Agriculture  
**Problem:** Many small farms keep harvest records in notebooks or not at all, so it is hard to compare plots or see whether yields are improving. This tool gives farms a free, lightweight way to track yields on any computer with Python.

## Features

- Register a crop plot (plot label, crop name, size in hectares) with an automatically generated ID
- Record harvests for each plot (season and weight in kg)
- Show all plots with their harvests, average yield per hectare, and a simple Low / Medium / High rating
- Remove a plot's record
- Find the plot with the best average yield

## How to Run

1. Install Python 3.8 or later.
2. Download or clone this repository:
   
3. Run the program:
   ```
   python crop_yield_monitor.py
   ```

The program starts empty and opens a menu. You add your own plots:

```
1. Add plot  2. Record harvest  3. Show all
4. Remove plot  5. Best yield  6. Exit
```

Sample data is available but does not run by default: call `demo(registry)` in the last lines of the file to load it.

## Project Structure

| File | Purpose |
|------|---------|
| `crop_yield_monitor.py` | Classes, demo and menu |
| `README.md` | Documentation |
| `LICENSE` | MIT open-source licence |

## OOP Concepts Used

### Task 1: Classes and Objects
- **`Crop`**: attributes `crop_id`, `plot_label`, `crop_name`, `area_ha`, `harvests`; methods `add_harvest()`, `update_record()`, `average_yield()`, `display_info()`
- **`FarmRegistry`**: attributes `farm_name`, `crops`; methods `add_crop()`, `find()`, `display_all()`, `remove_crop()`, `best_yield()`
- The registry holds and manages `Crop` objects, which demonstrates interaction between objects. `best_yield()` asks each crop for its `average_yield()` and compares them.

### Task 2: Data Structure
- A **dictionary** (`{crop_id: Crop}`) stores all plots, so any record can be found instantly by its ID.
- `add_crop()` and `display_all()` add and display records.
- **Bonus:** each harvest is a **tuple** `(season, yield_kg)`, and a plot's `harvests` is a tuple of these. Tuples cannot be changed, so each new harvest builds a new tuple. The dictionary is the only data structure holding the plot objects.

### Task 3: Methods
| Type | Method | Purpose |
|------|--------|---------|
| Instance | `add_harvest()`, `update_record()`, `average_yield()`, `display_info()` | Work on one plot's data |
| Class (`@classmethod`) | `Crop.from_string("Plot A, Cassava, 2.5")` | Alternative way to create a plot from text |
| Static (`@staticmethod`) | `Crop.kg_per_hectare()`, `Crop.yield_rating()` | Helpers that need no object: convert a harvest to kg per hectare, and give a general rating |

## Digital Public Goods (DPG) Alignment

| DPG Principle | How this project meets it |
|---------------|---------------------------|
| **Open-source** | The full source code is public on GitHub under the MIT licence, so anyone can use, study, modify and share it. |
| **Inclusive and accessible design** | Uses plain-language prompts and clear error messages, including messages for wrongly typed sizes or yields. It runs on any low-spec computer, needs no internet connection and has no cost. |
| **Privacy-respecting** | No personal data about farmers is stored. Each record is a plot label (such as "Plot A"), a crop name, a size and harvest figures. There are no names, phone numbers, addresses, ID numbers or exact GPS locations. Data is kept in memory only and is not sent anywhere. A plot record can be removed at any time. |
| **Modular and reusable** | `Crop` and `FarmRegistry` are separate, self-contained classes. They can be imported into other projects, for example a livestock tracker or a market price tool, without changing the code. |

## Sample Output

```
1. Add plot  2. Record harvest  3. Show all
4. Remove plot  5. Best yield  6. Exit
Choose: 1
Plot,crop,hectares (e.g. Plot A,Maize,1.5): Plot A,Cassava,2.5
Added Plot A (Cassava) with ID C001.

Choose: 2
Plot ID: c001
Season (e.g. 2026 Wet season): 2026 Wet season
Yield in kg: 5000

Choose: 3

=== Community Farm: 1 plot(s) ===
ID: C001 | Plot A | Cassava | 2.5 ha | Harvests: 1
    - 2026 Wet season: 5000.0 kg
    Average: 2000.0 kg/ha (Medium)

Choose: 5
Best yield: Plot A (Cassava) with 2000.0 kg/ha.
```

## Limitations and Future Improvements

- Records are lost when the program closes (kept in memory for privacy). A future version could add optional local storage.
- The Low / Medium / High rating is general. Real targets differ for each crop, so a future version could use crop-specific values.
- Add a graphical interface and local-language support (e.g. Krio).

## Author

Amadu Lamrana Bah

## Licence

Released under the [MIT Licence](LICENSE).
