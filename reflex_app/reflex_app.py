"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    label = "Welcome to Reflex!"

    def handle_title_on_change(self, val):
        self.label = val
    
    def did_click(self):
        print("The event on click")

def base_page(*args) -> rx.Component:
    print([type(x) for x in args])
    return rx.container(
        *args,
        rx.color_mode.button(position="top-right"),
        rx.logo(),
    )

def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.input(
                default_value=State.label,
                on_click=State.did_click,
                on_change=State.handle_title_on_change
                ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        
    )


app = rx.App()
app.add_page(index)
