module.exports = {
  env: {
    browser: true,
    node: true,
    es2021: true,
  },
  extends: ["eslint:recommended"],
  parserOptions: {
    ecmaVersion: "latest",
    sourceType: "module",
  },
  rules: {
    // Add any custom rules here, e.g.
    "no-unused-vars": "warn",
    semi: ["error", "always"],
    quotes: ["error", "double"],
  },
};
