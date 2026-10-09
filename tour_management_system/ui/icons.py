from html import escape


ICONS = {
    "plane": "M2 16.5 22 3l-6 18-4-8-8 2 8-5-4-8z",
    "search": "M21 21l-4.35-4.35M10.5 18a7.5 7.5 0 1 1 0-15 7.5 7.5 0 0 1 0 15z",
    "calendar": "M7 2v4M17 2v4M3 10h18M5 5h14a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2z",
    "users": "M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75",
    "wallet": "M20 7H4a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2zM16 7V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v4M18 13h.01",
    "chart": "M3 3v18h18M8 17V9M13 17V5M18 17v-7",
    "check": "M20 6 9 17l-5-5",
    "x": "M18 6 6 18M6 6l12 12",
    "map": "M9 18l-6 3V6l6-3 6 3 6-3v15l-6 3-6-3zM9 3v15M15 6v15",
    "spark": "M12 2l1.9 6.1L20 10l-6.1 1.9L12 18l-1.9-6.1L4 10l6.1-1.9L12 2z",
    "download": "M12 3v12M7 10l5 5 5-5M5 21h14",
}


def icon(name: str, size: int = 20, css_class: str = "ui-icon") -> str:
    path = ICONS.get(name, ICONS["spark"])
    return (
        f"<svg class='{escape(css_class)}' width='{size}' height='{size}' viewBox='0 0 24 24' "
        "fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' "
        f"stroke-linejoin='round' aria-hidden='true'><path d='{path}'/></svg>"
    )
