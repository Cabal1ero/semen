/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    // Шаблоны Django
    '../templates/**/*.html',
    '../../templates/**/*.html',
    // JavaScript файлы (если есть)
    './src/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
  // Новые опции, доступные в Tailwind 4.x
  future: {
    hoverOnlyWhenSupported: true,
  },
  darkMode: 'class', // или 'media' для определения по системным настройкам
}
