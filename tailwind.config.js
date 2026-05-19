/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        cream: '#fff8ea',
        butter: '#ffe89c',
        peach: '#ffc8a9',
        blush: '#ffd9e6',
        lilac: '#c9b8ff',
        sky: '#ace3ff',
        ink: '#574766',
      },
      boxShadow: {
        soft: '0 24px 60px rgba(116, 85, 138, 0.16)',
        card: '0 14px 30px rgba(116, 85, 138, 0.12)',
      },
      fontFamily: {
        display: ['Nunito', 'ui-rounded', 'system-ui', 'sans-serif'],
        body: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
