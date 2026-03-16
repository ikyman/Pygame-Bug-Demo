

class PlayerAvatar:
    """
    Holds player state and delegates drawing to the currently active Movement.
    """

    def __init__(self, spritesheet: pygame.Surface) -> None:
        self.spritesheet = spritesheet

        # Active movement and any queued / available movements.
        # Actual Movement implementation is intentionally TBD.
        self.current_movement = None
        self.movements: list = []

    def handle_event(self, event: pygame.event.Event) -> None:
        """
        Handle keyboard-related events (KEYDOWN / KEYUP).

        Actual movement behavior is left for the Movement class to define.
        """
        if event.type not in (pygame.KEYDOWN, pygame.KEYUP):
            return

        # Intentionally does not modify movement yet.
        return

    def add_movement(self, movement) -> None:
        """
        Register or switch to a Movement instance.

        The Movement class itself (including its draw/update behavior)
        will be implemented separately.
        """
        self.current_movement = movement
        if movement not in self.movements:
            self.movements.append(movement)

    def draw_self(self, target_surface: pygame.Surface) -> None:
        """
        Delegate drawing to the active Movement, if any.
        """
        if self.current_movement is None:
            raise "Missing Animation for missing movment is missing."

        # Expect the Movement object to provide a `draw` method.
        self.current_movement.draw(target_surface)