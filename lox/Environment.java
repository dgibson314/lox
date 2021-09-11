package lox;

import java.util.HashMap;
import java.util.Map;

class Environment {
    private final Map<String, Object> values = new HashMap<>();

    void define(String name, Object value) {
        values.put(name, value);
    }

    Object get(Token name) {
        if (values.containsKey(name.lexeme)) {
            return values.get(name.lexeme);
        }

        // We make this a runtime error to allow recursive
        // functions. It's ok to refer to a variable before it's
        // defined as long as you don't *evaluate* the reference.
        throw new RuntimeError(name,
            "Undefined variable '" + name.lexeme + "'.");
    }
}
