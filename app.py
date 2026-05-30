import streamlit as st

# =========================================================
# RECETTES
# =========================================================

recipes = {

    "Cake poulet curry": {

        "Farine": {
            "qty": 200,
            "unit": "g",
            "price": 0.30
        },

        "Levure chimique": {
            "qty": 1,
            "unit": "sachet",
            "price": 0.15
        },

        "Œufs": {
            "qty": 3,
            "unit": "pcs",
            "price": 0.75
        },

        "Lait": {
            "qty": 100,
            "unit": "ml",
            "price": 0.12
        },

        "Huile": {
            "qty": 80,
            "unit": "ml",
            "price": 0.25
        },

        "Poulet cuit": {
            "qty": 150,
            "unit": "g",
            "price": 2.50
        },

        "Fromage râpé": {
            "qty": 100,
            "unit": "g",
            "price": 1.00
        },

        "Curry": {
            "qty": 2,
            "unit": "cc",
            "price": 0.20
        },

        "Sel": {
            "qty": 1,
            "unit": "pincée",
            "price": 0.02
        },

        "Poivre": {
            "qty": 1,
            "unit": "pincée",
            "price": 0.05
        }
    },

    "Cake jambon champignons": {

        "Farine": {
            "qty": 200,
            "unit": "g",
            "price": 0.30
        },

        "Levure chimique": {
            "qty": 1,
            "unit": "sachet",
            "price": 0.15
        },

        "Œufs": {
            "qty": 3,
            "unit": "pcs",
            "price": 0.75
        },

        "Lait": {
            "qty": 100,
            "unit": "ml",
            "price": 0.12
        },

        "Huile": {
            "qty": 80,
            "unit": "ml",
            "price": 0.25
        },

        "Jambon": {
            "qty": 150,
            "unit": "g",
            "price": 2.00
        },

        "Champignons": {
            "qty": 150,
            "unit": "g",
            "price": 1.50
        },

        "Fromage râpé": {
            "qty": 100,
            "unit": "g",
            "price": 1.00
        },

        "Sel": {
            "qty": 1,
            "unit": "pincée",
            "price": 0.02
        },

        "Poivre": {
            "qty": 1,
            "unit": "pincée",
            "price": 0.05
        }
    },

    "Cake chorizo poivrons": {

        "Farine": {
            "qty": 200,
            "unit": "g",
            "price": 0.30
        },

        "Levure chimique": {
            "qty": 1,
            "unit": "sachet",
            "price": 0.15
        },

        "Œufs": {
            "qty": 3,
            "unit": "pcs",
            "price": 0.75
        },

        "Lait": {
            "qty": 100,
            "unit": "ml",
            "price": 0.12
        },

        "Huile": {
            "qty": 80,
            "unit": "ml",
            "price": 0.25
        },

        "Chorizo": {
            "qty": 150,
            "unit": "g",
            "price": 2.50
        },

        "Poivrons": {
            "qty": 1,
            "unit": "pcs",
            "price": 0.80
        },

        "Fromage râpé": {
            "qty": 100,
            "unit": "g",
            "price": 1.00
        },

        "Sel": {
            "qty": 1,
            "unit": "pincée",
            "price": 0.02
        },

        "Poivre": {
            "qty": 1,
            "unit": "pincée",
            "price": 0.05
        }
    },

    "Cake thon olives": {

        "Farine": {
            "qty": 200,
            "unit": "g",
            "price": 0.30
        },

        "Levure chimique": {
            "qty": 1,
            "unit": "sachet",
            "price": 0.15
        },

        "Œufs": {
            "qty": 3,
            "unit": "pcs",
            "price": 0.75
        },

        "Lait": {
            "qty": 100,
            "unit": "ml",
            "price": 0.12
        },

        "Huile": {
            "qty": 80,
            "unit": "ml",
            "price": 0.25
        },

        "Thon": {
            "qty": 140,
            "unit": "g",
            "price": 2.00
        },

        "Olives vertes": {
            "qty": 100,
            "unit": "g",
            "price": 1.20
        },

        "Fromage râpé": {
            "qty": 100,
            "unit": "g",
            "price": 1.00
        },

        "Sel": {
            "qty": 1,
            "unit": "pincée",
            "price": 0.02
        },

        "Poivre": {
            "qty": 1,
            "unit": "pincée",
            "price": 0.05
        }
    },
    
    "Mini burger bœuf": {

        "Mini buns": {
            "qty": 9,
            "unit": "pièce",
            "price": 0
        },

        "Sauce burger": {
            "qty": 90,
            "unit": "g",
            "price": 0
        },

        "Cornichons": {
            "qty": 9,
            "unit": "rondelle",
            "price": 0
        },

        "Salade": {
            "qty": 90,
            "unit": "g",
            "price": 0
        },

        "Steack de bœuf": {
            "qty": 180,
            "unit": "g",
            "price": 0
        },

        "Oignons frits": {
            "qty": 45,
            "unit": "g",
            "price": 0
        },

        "Cheddar": {
            "qty": 2.25,
            "unit": "tranche",
            "price": 0
        }
    },

    "Mini burger poulet": {

        "Mini buns": {
            "qty": 9,
            "unit": "pièce",
            "price": 0
        },

        "Sauce burger": {
            "qty": 90,
            "unit": "g",
            "price": 0
        },

        "Cornichons": {
            "qty": 9,
            "unit": "rondelle",
            "price": 0
        },

        "Salade": {
            "qty": 90,
            "unit": "g",
            "price": 0
        },

        "Nuggets": {
            "qty": 9,
            "unit": "pièce",
            "price": 0
        },

        "Oignons frits": {
            "qty": 45,
            "unit": "g",
            "price": 0
        },

        "Cheddar": {
            "qty": 2.25,
            "unit": "tranche",
            "price": 0
        }
    },

    "Wraps poulet": {

        "Wrap": {
            "qty": 2.25,
            "unit": "wrap",
            "price": 0
        },

        "Poulet": {
            "qty": 3,
            "unit": "pané de poulet",
            "price": 0
        },

        "Salade": {
            "qty": 180,
            "unit": "g",
            "price": 0
        },

        "Sauce frite": {
            "qty": 90,
            "unit": "g",
            "price": 0
        }
    },

    "Tartelettes 10": {

        "Crème pâtissière": {

            "Lait entier": {"qty": 500, "unit": "ml", "price": 0.60},
            "Jaunes d’œufs": {"qty": 4, "unit": "pcs", "price": 1.00},
            "Sucre": {"qty": 100, "unit": "g", "price": 0.15},
            "Maïzena": {"qty": 40, "unit": "g", "price": 0.20},
            "Beurre": {"qty": 30, "unit": "g", "price": 0.35},
            "Vanille": {"qty": 1, "unit": "cc", "price": 0.50},
        },

        "Chantilly mascarpone": {

            "Mascarpone": {"qty": 250, "unit": "g", "price": 2.20},
            "Crème liquide entière": {"qty": 400, "unit": "ml", "price": 2.00},
            "Sucre glace": {"qty": 60, "unit": "g", "price": 0.20},
        }
    },

    "Muffins chorizo poivrons": {

        "Farine": {"qty": 300, "unit": "g", "price": 0.45},
        "Levure chimique": {"qty": 1, "unit": "sachet", "price": 0.15},
        "Œufs": {"qty": 4, "unit": "pcs", "price": 1.00},
        "Lait": {"qty": 200, "unit": "ml", "price": 0.25},
        "Huile": {"qty": 100, "unit": "ml", "price": 0.30},
        "Chorizo": {"qty": 150, "unit": "g", "price": 2.50},
        "Poivrons": {"qty": 2, "unit": "pcs", "price": 1.50},
    },

    "Gaufres (10 classiques)": {

        "Farine": {"qty": 250, "unit": "g", "price": 0.35},
        "Œufs": {"qty": 2, "unit": "pcs", "price": 0.50},
        "Lait": {"qty": 500, "unit": "ml", "price": 0.60},
        "Beurre fondu": {"qty": 100, "unit": "g", "price": 1.10},
        "Sucre": {"qty": 40, "unit": "g", "price": 0.08},
    }
    
"Madeleines Chorizo & Paprika (5 pièces)": {

        "Farine": {
            "qty": 25,
            "unit": "g",
            "price": 0.03
        },

        "Œufs": {
            "qty": 0.5,
            "unit": "pcs",
            "price": 0.15
        },

        "Levure": {
            "qty": 1.25,
            "unit": "g",
            "price": 0.01
        },

        "Beurre": {
            "qty": 20,
            "unit": "g",
            "price": 0.18
        },

        "Chorizo": {
            "qty": 20,
            "unit": "g",
            "price": 0.23
        },

        "Emmental": {
            "qty": 15,
            "unit": "g",
            "price": 0.15
        }
    },


    "Madeleines Saumon & Aneth (5 pièces)": {

        "Farine": {
            "qty": 25,
            "unit": "g",
            "price": 0.03
        },

        "Œufs": {
            "qty": 0.5,
            "unit": "pcs",
            "price": 0.15
        },

        "Levure": {
            "qty": 1.25,
            "unit": "g",
            "price": 0.01
        },

        "Beurre": {
            "qty": 20,
            "unit": "g",
            "price": 0.18
        },

        "Saumon fumé": {
            "qty": 15,
            "unit": "g",
            "price": 0.55
        },

        "Aneth": {
            "qty": 0.25,
            "unit": "cs",
            "price": 0.04
        }
    },


    "Madeleines Parmesan & Tomate Séchée (5 pièces)": {

        "Farine": {
            "qty": 25,
            "unit": "g",
            "price": 0.03
        },

        "Œufs": {
            "qty": 0.5,
            "unit": "pcs",
            "price": 0.15
        },

        "Levure": {
            "qty": 1.25,
            "unit": "g",
            "price": 0.01
        },

        "Beurre": {
            "qty": 20,
            "unit": "g",
            "price": 0.18
        },

        "Parmesan": {
            "qty": 12.5,
            "unit": "g",
            "price": 0.23
        },

        "Tomates séchées": {
            "qty": 12.5,
            "unit": "g",
            "price": 0.20
        }
    },


    "Madeleines Chèvre Miel Noix (5 pièces)": {

        "Farine": {
            "qty": 25,
            "unit": "g",
            "price": 0.03
        },

        "Œufs": {
            "qty": 0.5,
            "unit": "pcs",
            "price": 0.15
        },

        "Levure": {
            "qty": 1.25,
            "unit": "g",
            "price": 0.01
        },

        "Beurre": {
            "qty": 20,
            "unit": "g",
            "price": 0.18
        },

        "Chèvre frais": {
            "qty": 17.5,
            "unit": "g",
            "price": 0.28
        },

        "Miel": {
            "qty": 0.25,
            "unit": "cs",
            "price": 0.05
        },

        "Noix": {
            "qty": 7.5,
            "unit": "g",
            "price": 0.13
        }
    },


    "Madeleines Jambon Cru & Parmesan (5 pièces)": {

        "Farine": {
            "qty": 25,
            "unit": "g",
            "price": 0.03
        },

        "Œufs": {
            "qty": 0.5,
            "unit": "pcs",
            "price": 0.15
        },

        "Levure": {
            "qty": 1.25,
            "unit": "g",
            "price": 0.01
        },

        "Beurre": {
            "qty": 20,
            "unit": "g",
            "price": 0.18
        },

        "Jambon cru": {
            "qty": 15,
            "unit": "g",
            "price": 0.33
        },

        "Parmesan": {
            "qty": 12.5,
            "unit": "g",
            "price": 0.23
        }
    },


    "Madeleines Feta & Olive Noire (5 pièces)": {

        "Farine": {
            "qty": 25,
            "unit": "g",
            "price": 0.03
        },

        "Œufs": {
            "qty": 0.5,
            "unit": "pcs",
            "price": 0.15
        },

        "Levure": {
            "qty": 1.25,
            "unit": "g",
            "price": 0.01
        },

        "Beurre": {
            "qty": 20,
            "unit": "g",
            "price": 0.18
        },

        "Feta": {
            "qty": 17.5,
            "unit": "g",
            "price": 0.23
        },

        "Olives noires": {
            "qty": 10,
            "unit": "g",
            "price": 0.10
        }
    },


    "Madeleines Poulet Curry (5 pièces)": {

        "Farine": {
            "qty": 25,
            "unit": "g",
            "price": 0.03
        },

        "Œufs": {
            "qty": 0.5,
            "unit": "pcs",
            "price": 0.15
        },

        "Levure": {
            "qty": 1.25,
            "unit": "g",
            "price": 0.01
        },

        "Beurre": {
            "qty": 20,
            "unit": "g",
            "price": 0.18
        },

        "Poulet": {
            "qty": 17.5,
            "unit": "g",
            "price": 0.23
        },

        "Curry doux": {
            "qty": 0.25,
            "unit": "cc",
            "price": 0.02
        }
    },


    "Madeleines Poivron & Comté (5 pièces)": {

        "Farine": {
            "qty": 25,
            "unit": "g",
            "price": 0.03
        },

        "Œufs": {
            "qty": 0.5,
            "unit": "pcs",
            "price": 0.15
        },

        "Levure": {
            "qty": 1.25,
            "unit": "g",
            "price": 0.01
        },

        "Beurre": {
            "qty": 20,
            "unit": "g",
            "price": 0.18
        },

        "Poivron grillé": {
            "qty": 15,
            "unit": "g",
            "price": 0.18
        },

        "Comté": {
            "qty": 15,
            "unit": "g",
            "price": 0.28
        }
    },
}

# =========================================================
# UTILITAIRES
# =========================================================

def collect_ingredients(recipe_dict, storage):
    for ing, data in recipe_dict.items():
        if "qty" in data:
            if ing not in storage:
                storage[ing] = data
        else:
            collect_ingredients(data, storage)


def update_prices(recipes_dict, prices):
    for ing, new_price in prices.items():

        def recurse(d):
            for k, v in d.items():
                if "qty" in v:
                    if k == ing:
                        v["price"] = new_price
                else:
                    recurse(v)

        for r in recipes_dict.values():
            recurse(r)


def compute_shopping_list(selected, recipes_dict):
    total = {}

    for recipe_name, qty in selected.items():

        if qty <= 0:
            continue

        def recurse(data):

            for ing, v in data.items():

                if "qty" in v:

                    if ing not in total:
                        total[ing] = {
                            "qty": 0,
                            "cost": 0,
                            "unit": v["unit"]
                        }

                    total[ing]["qty"] += v["qty"] * qty
                    total[ing]["cost"] += v["price"] * qty

                else:
                    recurse(v)

        recurse(recipes_dict[recipe_name])

    return total


# =========================================================
# STREAMLIT UI
# =========================================================

st.title("🛒 Liste de courses intelligente")

st.write("Choisis tes recettes, ajuste les prix et génère ta liste automatiquement.")

# =========================================================
# QUANTITÉS RECETTES
# =========================================================

st.subheader("🍽️ Quantité de recettes")

selected_quantities = {}

cols = st.columns(2)

for i, recipe in enumerate(recipes.keys()):
    with cols[i % 2]:
        selected_quantities[recipe] = st.number_input(
            recipe,
            min_value=0,
            max_value=20,
            value=0,
            step=1
        )

# =========================================================
# PRIX UNITAIRES
# =========================================================

st.subheader("💰 Prix unitaires")

all_ingredients = {}

for r in recipes.values():
    collect_ingredients(r, all_ingredients)

prices = {}

for ing, data in all_ingredients.items():
    prices[ing] = st.number_input(
        f"{ing} ({data['unit']})",
        value=float(data["price"]),
        step=0.05
    )

# =========================================================
# BOUTON GÉNÉRATION
# =========================================================

if st.button("📦 Générer la liste de courses"):

    update_prices(recipes, prices)

    result = compute_shopping_list(selected_quantities, recipes)

    if not result:
        st.warning("Aucune recette sélectionnée.")
    else:

        st.subheader("🧾 Liste de courses")

        total_global = 0

        for ing, data in result.items():

            st.write(
                f"**{ing}** : {data['qty']} {data['unit']} "
                f"→ {data['cost']:.2f} €"
            )

            total_global += data["cost"]

        st.success(f"💰 TOTAL : {total_global:.2f} €")
