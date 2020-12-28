from django.db import models
from django_fsm import FSMField, TransitionNotAllowed


class FsmMixin(models.Model):
    state = FSMField(
        default="created"
    )

    @property
    def available_transitions(self):
        """ Retorna las transiciones disponibles para el objeto dado """
        this_states = self.get_available_state_transitions()
        available_states = []
        for items in this_states:
            available_states.append(items.name)
        return available_states

    # Transiciones de la maquina de estados
    def execute_transition(self, transition_name: str, data: dict = None):
        """
        Metodo para ejecutar una transicion
        :param transition_name:
        :param data:
        :return:
        """
        executable_transition = getattr(
            self,
            transition_name,
            lambda params: (_ for _ in ()).throw(TransitionNotAllowed),
        )
        return executable_transition(data)

    class Meta:
        abstract = True


class TransitionsMixin(models.Model):
    USER_TYPE = (
        ("AGENT", "Colaborador Inmobilio"),
        ("CONTACT", "Usuario")
    )

    triggered_by = models.CharField(
        "User email",
        max_length=100,
        null=True
    )

    triggered_by_user = models.CharField(
        "User type",
        choices=USER_TYPE,
        max_length=20,
        null=True,
    )

    transition = models.CharField(
        "Name of the transition",
        max_length=100,
        null=True,
    )

    from_state = models.CharField(
        "Name of the states it comes",
        max_length=100,
        null=True,
    )

    to_state = models.CharField(
        "Name of the state if goes",
        max_length=100,
        null=True,
    )

    def __str__(self):
        return self.transition

    class Meta:
        abstract = True
