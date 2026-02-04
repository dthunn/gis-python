import matplotlib.pyplot as plt
from shapely.geometry.base import BaseGeometry

def plot_geometries(geom1: BaseGeometry, geom2: BaseGeometry):
    """
    Plot any two Shapely geometry objects with basic styling.
    """
    fig, ax = plt.subplots(figsize=(6, 6))

    def plot_geom(geom, color, label):
        if geom.geom_type == 'Point':
            ax.plot(*geom.xy, 'o', color=color, label=label)
        elif geom.geom_type in ['LineString', 'LinearRing']:
            x, y = geom.xy
            ax.plot(x, y, color=color, linewidth=2, label=label)
        elif geom.geom_type == 'Polygon':
            x, y = geom.exterior.xy
            ax.fill(x, y, alpha=0.5, fc=color, ec='black', label=label)
        elif geom.geom_type.startswith('Multi'):
            for part in geom.geoms:
                plot_geom(part, color, label)
        else:
            print(f"Geometry type {geom.geom_type} not supported for plotting.")

    # Plot both geometries
    plot_geom(geom1, 'blue', 'Geometry 1')
    plot_geom(geom2, 'red', 'Geometry 2')

    ax.set_aspect('equal')
    ax.legend()
    ax.grid(True)
    ax.set_title(f"{geom1.geom_type} and {geom2.geom_type}")
    plt.show()

def plot_three_geometries(geom1: BaseGeometry, geom2: BaseGeometry, geom3: BaseGeometry):
    """
    Plot any three Shapely geometry objects with basic styling.
    """
    fig, ax = plt.subplots(figsize=(6, 6))

    def plot_geom(geom, color, label):
        if geom.geom_type == 'Point':
            ax.plot(*geom.xy, 'o', color=color, label=label)
        elif geom.geom_type in ['LineString', 'LinearRing']:
            x, y = geom.xy
            ax.plot(x, y, color=color, linewidth=2, label=label)
        elif geom.geom_type == 'Polygon':
            x, y = geom.exterior.xy
            ax.fill(x, y, alpha=0.5, fc=color, ec='black', label=label)
        elif geom.geom_type.startswith('Multi'):
            for part in geom.geoms:
                plot_geom(part, color, label)
        else:
            print(f"Geometry type {geom.geom_type} not supported for plotting.")

    # Plot all geometries
    plot_geom(geom1, 'red', 'Geometry 1')
    plot_geom(geom2, 'blue', 'Geometry 2')
    plot_geom(geom3, 'green', 'Geometry 3')

    ax.set_aspect('equal')
    ax.legend()
    ax.grid(True)
    ax.set_title(f"{geom1.geom_type}, {geom2.geom_type}, and {geom3.geom_type}")
    plt.show()
