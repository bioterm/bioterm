module.exports = {
  extends: ["@commitlint/config-conventional"],
  rules: {
    "header-max-length": [0, "always", 72],
    "scope-empty": [2, "never"],
    "scope-enum": [
      2,
      "always",
      [
        "common",
        "controller",
        "devices",
        "server",
        "server--backend",
        "server--frontend",
        "deployment",
        "development",
      ],
    ],
  },
};
