import reflex as rx
from .nav import navbar
def base_page(child: rx.Component, hide_navbar=False, *args, **kwargs) -> rx.Component:
    if not isinstance(child, rx.Component):
        child = rx.heading("This is not a valid child! element here", size="6"),
    
    if hide_navbar:
        return rx.container(
            child,
            rx.color_mode.button(position="bottom-left"),
            rx.logo(),
        )
    return rx.fragment(
        navbar(),
        rx.box(
            child,
            # bg=rx.color("accent", 3),
            padding="1em",
            # text_align="center",
            width="100%",
            id="my-content-area-el"
            ),
        rx.color_mode.button(position="bottom-left"),
        rx.logo(),
        padding="10em",
        id="my-base-container"
    )