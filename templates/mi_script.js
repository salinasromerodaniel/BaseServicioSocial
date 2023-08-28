
    // Obtener el elemento del menú desplegable
    const selectElement = document.getElementById('sistema_operativo');

    // Evento de cambio en el menú desplegable
    selectElement.addEventListener('change', (event) => {
        // Obtener la opción seleccionada
        const selectedOption = event.target.selectedOptions[0];
        
        // Obtener los atributos de datos asociados con la opción seleccionada
        const sistemaId = selectedOption.getAttribute('value');
        const version = selectedOption.getAttribute('data-version');
        const arquitectura = selectedOption.getAttribute('data-arquitectura');
        
        // Hacer lo que necesites con los valores obtenidos
        console.log("SISTEMA_OPERATIVO_ID:", sistemaId);
        console.log("Versión:", version);
        console.log("Arquitectura:", arquitectura);
    });


function obtenerModeloId() {
        const selectElement = document.getElementById('modelo');
        const selectedOption = selectElement.selectedOptions[0];
        const modeloId = selectedOption.getAttribute('value');
        console.log("MODELO_ID:", modeloId);
    }
document.addEventListener('DOMContentLoaded', function() {
    // Obtener el elemento select y el elemento oculto para almacenar el RESPONSABLE_RESGUARDO_ID
    const selectResguardo = document.getElementById('resguardo');
    const inputResguardoId = document.getElementById('resguardo_id');

    // Agregar un evento para detectar el cambio en el menú deslizable de responsable de resguardo
    selectResguardo.addEventListener('change', function() {
        // Obtener el valor seleccionado en el menú deslizable (RESPONSABLE_RESGUARDO_ID)
        const selectedId = selectResguardo.options[selectResguardo.selectedIndex].value;

        // Almacenar el RESPONSABLE_RESGUARDO_ID en el elemento oculto
        inputResguardoId.value = selectedId;
    });

    // Obtener el elemento select y el elemento oculto para almacenar el RESPONSABLE_INTERNO_ID
    const selectInterno = document.getElementById('interno');
    const inputInternoId = document.getElementById('interno_id');

    // Agregar un evento para detectar el cambio en el menú deslizable de responsable interno
    selectInterno.addEventListener('change', function() {
        // Obtener el valor seleccionado en el menú deslizable (RESPONSABLE_INTERNO_ID)
        const selectedId = selectInterno.options[selectInterno.selectedIndex].value;

        // Almacenar el RESPONSABLE_INTERNO_ID en el elemento oculto
        inputInternoId.value = selectedId;
    });

    const selectUsuario = document.getElementById('usuario');
    const inputUsuarioId = document.getElementById('usuario_id');

    // Agregar un evento para detectar el cambio en el menú deslizable
    selectUsuario.addEventListener('change', function() {
        // Obtener el valor seleccionado en el menú deslizable (USUARIO_FINAL_ID)
        const selectedId = selectUsuario.options[selectUsuario.selectedIndex].value;

        // Almacenar el USUARIO_FINAL_ID en el elemento oculto
        inputUsuarioId.value = selectedId;
    });

    // Obtener el elemento select y el elemento oculto para almacenar el UBICACION_ID
    const selectUbicacion = document.getElementById('ubicacion');
    const inputUbicacionId = document.getElementById('ubicacion_id');

    // Agregar un evento para detectar el cambio en el menú deslizable
    selectUbicacion.addEventListener('change', function() {
        // Obtener el valor seleccionado en el menú deslizable (UBICACION_ID)
        const selectedId = selectUbicacion.options[selectUbicacion.selectedIndex].value;

        // Almacenar el UBICACION_ID en el campo oculto
        inputUbicacionId.value = selectedId;
    });

    // Obtener el elemento select y el elemento oculto para almacenar el SUBTIPO_ID
    const selectSubtipo = document.getElementById('subtipo');
    const inputSubtipoId = document.getElementById('subtipo_id');

    // Agregar un evento para detectar el cambio en el menú deslizable
    selectSubtipo.addEventListener('change', function() {
        // Obtener el valor seleccionado en el menú deslizable (SUBTIPO_ID)
        const selectedId = selectSubtipo.options[selectSubtipo.selectedIndex].value;

        // Almacenar el SUBTIPO_ID en el elemento oculto
        inputSubtipoId.value = selectedId;
    });

    // Obtener el div que contiene los checkboxes y el menú desplegable
    const ramUnitContainer = document.getElementById('ram_unit_container');
    const ramMaximaSelect = document.getElementById('ram_maxima');

    // Agregar un evento para detectar el cambio en los checkboxes
    ramUnitContainer.addEventListener('change', function() {
        // Obtener los checkboxes
        const gbCheckbox = document.getElementById('gb_checkbox');
        const tbCheckbox = document.getElementById('tb_checkbox');

        // Habilitar o deshabilitar el menú desplegable según la selección de los checkboxes
        ramMaximaSelect.disabled = !gbCheckbox.checked && !tbCheckbox.checked;

        // Si algún checkbox está seleccionado, reiniciar el menú desplegable a la opción predeterminada
        if (gbCheckbox.checked || tbCheckbox.checked) {
            ramMaximaSelect.selectedIndex = 0;
        }
    });

});



