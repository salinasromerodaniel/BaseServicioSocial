<script>
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
</script>
<script>
// Función para cargar los modelos asociados a una marca seleccionada
function cargarModelosPorMarca(marcaId) {
    // Realizar una solicitud AJAX al servidor para obtener los modelos
    $.ajax({
        type: "GET",
        url: "/obtener_modelos/" + marcaId,
        success: function (response) {
            // Si la solicitud es exitosa, actualizar el menú desplegable de modelos
            const selectModelo = document.getElementById('modelo');
            selectModelo.innerHTML = ''; // Limpiar las opciones existentes
            response.modelos.forEach(function (modelo) {
                const option = document.createElement('option');
                option.value = modelo;
                option.text = modelo;
                selectModelo.appendChild(option);
            });
        },
        error: function (error) {
            console.error("Error al obtener modelos:", error);
        }
    });
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

    // Obtener los elementos select para marca y modelo
    const selectMarca = document.getElementById('marca');
    const selectModelo = document.getElementById('modelo');

    // Función para actualizar el menú de modelos cuando se selecciona una marca
    function actualizarModelos() {
        const marcaSeleccionada = selectMarca.value;

        // Utilizar AJAX para enviar la marca seleccionada al servidor (ruta '/obtener_modelos') y recibir los modelos correspondientes
        fetch(`/obtener_modelos/${marcaSeleccionada}`)
            .then(response => response.json())
            .then(data => {
                // Limpiar el menú de modelos
                selectModelo.innerHTML = '';

                // Agregar las opciones de modelos correspondientes a la marca seleccionada
                data.modelos.forEach(function(modelo) {
                    const option = document.createElement('option');
                    option.text = modelo;
                    option.value = modelo;
                    selectModelo.add(option);
                });
            })
            .catch(error => {
                console.error('Error al obtener los modelos:', error);
            });
    }

    // Agregar un evento para detectar el cambio en el menú deslizable de marca
    selectMarca.addEventListener('change', function() {
        actualizarModelos();
    });

    // Ejecutar la función al cargar la página para asegurarse de que el menú de modelos esté actualizado inicialmente
    actualizarModelos();

});
</script>



