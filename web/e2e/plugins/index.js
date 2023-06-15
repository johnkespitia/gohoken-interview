// plugins/index.js

// Ejemplo de función que se ejecuta antes de cada prueba
beforeEach(() => {
    // Lógica a ejecutar antes de cada prueba
});

// Ejemplo de función que se ejecuta después de cada prueba
afterEach(() => {
    // Lógica a ejecutar después de cada prueba
});

// Ejemplo de función que se ejecuta antes de todas las pruebas
// before(() => {
//     // Lógica a ejecutar antes de todas las pruebas
// });
//
// // Ejemplo de función que se ejecuta después de todas las pruebas
// after(() => {
//     // Lógica a ejecutar después de todas las pruebas
// });

// También puedes exportar funciones personalizadas que puedes utilizar en tus pruebas
module.exports = {
    customFunction: () => {
        // Lógica de la función personalizada
    }
};
