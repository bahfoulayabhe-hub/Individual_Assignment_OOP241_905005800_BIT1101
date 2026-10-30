print("==================================================")
print("Crop Yield Monitoring System ")
print("==================================================")
# ---------------------------------------------------------------- Class 1
class Crop:
    """One crop plot and its harvests (Task 1: attributes + methods)."""

    _counter = 0  # class attribute used to generate unique IDs

    def __init__(self, plot_label, crop_name, area_ha):
        Crop._counter += 1
        self.crop_id = f"C{Crop._counter:03d}"
        self.plot_label = plot_label      # e.g. "Plot A" (no farmer name)
        self.crop_name = crop_name
        self.area_ha = area_ha            # plot size in hectares
        self.harvests = ()                # tuple of (season, yield_kg) tuples

    # ---- instance methods (Task 3)
    def add_harvest(self, season, yield_kg):
        """Record a harvest as an immutable tuple: (season, yield_kg).
        Tuples cannot be changed, so a new tuple of harvests is built."""
        new_harvest = (season, yield_kg)
        self.harvests = self.harvests + (new_harvest,)

    def update_record(self, plot_label=None, area_ha=None):
        if plot_label:
            self.plot_label = plot_label
        if area_ha is not None:
            self.area_ha = area_ha

    def average_yield(self):
        """Average yield in kg per hectare across all recorded harvests."""
        if not self.harvests:
            return 0.0
        total_kg = sum(kg for _, kg in self.harvests)
        return self.kg_per_hectare(total_kg / len(self.harvests), self.area_ha)

    def display_info(self):
        print(f"ID: {self.crop_id} | {self.plot_label} | {self.crop_name} | "
              f"{self.area_ha} ha | Harvests: {len(self.harvests)}")
        for season, yield_kg in self.harvests:
            print(f"    - {season}: {yield_kg} kg")
        if self.harvests:
            avg = self.average_yield()
            print(f"    Average: {avg} kg/ha ({self.yield_rating(avg)})")

    # ---- class method (Task 3)
    @classmethod
    def from_string(cls, text):
        """Create a Crop from 'plot,crop,area' e.g. 'Plot A, Cassava, 2.5'."""
        plot_label, crop_name, area = text.split(",")
        return cls(plot_label.strip(), crop_name.strip(), float(area))

    # ---- static methods (Task 3)
    @staticmethod
    def kg_per_hectare(total_kg, area_ha):
        """Convert a harvest weight and plot size to kg per hectare."""
        return round(total_kg / area_ha, 1)

    @staticmethod
    def yield_rating(kg_per_ha):
        """General rating only; real targets differ for each crop."""
        if kg_per_ha < 1000:
            return "Low"
        if kg_per_ha < 3000:
            return "Medium"
        return "High"


# ---------------------------------------------------------------- Class 2
class FarmRegistry:
    """Stores many Crop objects in a dictionary keyed by crop ID
    (Task 2: one data structure + add/display functions)."""

    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.crops = {}  # {crop_id: Crop}

    def add_crop(self, crop):
        self.crops[crop.crop_id] = crop
        print(f"Added {crop.plot_label} ({crop.crop_name}) with ID {crop.crop_id}.")

    def find(self, crop_id):
        return self.crops.get(crop_id.upper())

    def display_all(self):
        print(f"\n=== {self.farm_name}: {len(self.crops)} plot(s) ===")
        if not self.crops:
            print("No records yet.")
        for crop in self.crops.values():
            crop.display_info()

    def remove_crop(self, crop_id):
        """New function 1: delete a plot record."""
        removed = self.crops.pop(crop_id.upper(), None)
        if removed is None:
            print("Plot not found.")
            return False
        print(f"Record {removed.crop_id} ({removed.plot_label}) removed.")
        return True

    def best_yield(self):
        """New function 2: find the plot with the highest average yield."""
        best = None
        for crop in self.crops.values():
            if crop.harvests and (best is None
                                  or crop.average_yield() > best.average_yield()):
                best = crop
        if best is None:
            print("No harvests recorded yet.")
        else:
            print(f"Best yield: {best.plot_label} ({best.crop_name}) with "
                  f"{best.average_yield()} kg/ha.")
        return best


# ---------------------------------------------------------------- Demo / menu
def demo(registry):
    """Optional sample data. Not run by default; call demo(registry) to load it."""
    c1 = Crop("Plot A", "Cassava", 2.5)
    c2 = Crop.from_string("Plot B, Rice, 1.0")   # class method
    registry.add_crop(c1)
    registry.add_crop(c2)
    c1.add_harvest("2026 Wet season", 5000)      # instance method
    c2.add_harvest("2026 Wet season", 2500)
    c1.update_record(area_ha=2.0)
    registry.display_all()


def menu(registry):
    while True:
        print("\n1. Add plot  2. Record harvest  3. Show all")
        print("4. Remove plot  5. Best yield  6. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            try:
                c = Crop.from_string(input("Plot,crop,hectares (e.g. Plot A,Maize,1.5): "))
                if c.area_ha <= 0:
                    raise ValueError
                registry.add_crop(c)
            except ValueError:
                print("Please use the format: plot,crop,hectares (size above 0)")
        elif choice == "2":
            c = registry.find(input("Plot ID: "))
            if c:
                try:
                    season = input("Season (e.g. 2026 Wet season): ").strip()
                    c.add_harvest(season, float(input("Yield in kg: ")))
                except ValueError:
                    print("Yield must be a number.")
            else:
                print("Plot not found.")
        elif choice == "3":
            registry.display_all()
        elif choice == "4":
            registry.remove_crop(input("Plot ID to remove: "))
        elif choice == "5":
            registry.best_yield()
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    registry = FarmRegistry("Community Farm")
    menu(registry)  # starts empty; use demo(registry) for sample data
