import plotly.io as pio


BRAND_COLORS = ["#14B8A6", "#22D3EE", "#FF8A3D", "#12356B", "#16A34A", "#F59E0B", "#DC2626"]


def apply_plotly_theme():
    template = {
        "layout": {
            "font": {"family": "Inter, Segoe UI, sans-serif", "color": "#0F172A"},
            "paper_bgcolor": "rgba(0,0,0,0)",
            "plot_bgcolor": "rgba(0,0,0,0)",
            "colorway": BRAND_COLORS,
            "hoverlabel": {
                "bgcolor": "#0B1F3A",
                "font": {"color": "#FFFFFF", "family": "Inter, Segoe UI, sans-serif"},
                "bordercolor": "#14B8A6",
            },
            "xaxis": {"gridcolor": "rgba(100,116,139,.14)", "zerolinecolor": "rgba(100,116,139,.18)"},
            "yaxis": {"gridcolor": "rgba(100,116,139,.14)", "zerolinecolor": "rgba(100,116,139,.18)"},
            "legend": {"orientation": "h", "y": -0.18},
            "margin": {"l": 20, "r": 20, "t": 52, "b": 34},
        }
    }
    pio.templates["tour_premium"] = template
    pio.templates.default = "tour_premium"


def polish(fig, title: str | None = None):
    fig.update_layout(transition={"duration": 650, "easing": "cubic-in-out"})
    if title:
        fig.update_layout(title={"text": title, "x": 0.02, "xanchor": "left"})
    return fig
