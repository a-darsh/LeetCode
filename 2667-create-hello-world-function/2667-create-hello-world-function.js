/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        //args[] = "Hello World"
        return "Hello World"

    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */