/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './thesis/templates/**/*.html',
    './thesis/dashboard/templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ]
}
