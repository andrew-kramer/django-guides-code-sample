const ThemeSwapper = require('tailwindcss-theme-swapper')

module.exports = {
  purge: {
    // Only enable Purge in production mode to avoid constant rebuilds in development
    enabled: process.env.NODE_ENV === 'production',
    content: [
      './src/**/*.vue',
      './public/**/*.html'
    ]
  },
  darkMode: false,
  theme: {
    fontFamily: {
      brand: ['Consolas', 'monaco', 'monospace'],
      title: ['Calisto\\ MT, Bookman\\ Old\\ Style, Bookman, Goudy\\ Old\\ Style, Garamond, Hoefler\\ Text, Bitstream\\ Charter, Georgia, serif']
    },
    extend: {
    }
  },
  variants: {},
  plugins: [
    ThemeSwapper({
      themes: [
        {
          name: 'base',
          selectors: [':root'],
          theme: {
            colors: {
              primary: { // Forest Green
                900: '#10451D',
                800: '#155D27',
                700: '#1A7431',
                600: '#208B3A',
                500: '#25A244',
                400: '#2DC653',
                300: '#4AD66D',
                200: '#6EDE8A',
                100: '#92E6A7',
                50: '#B7EFC5'
              },
              secondary: { // Cool Gray
                900: '#111827',
                800: '#1F2937',
                700: '#374151',
                600: '#4B5563',
                500: '#6B7280',
                400: '#9CA3AF',
                300: '#D1D5DB',
                200: '#E5E7EB',
                100: '#F3F4F6',
                50: '#F9FAFB'
              }
            }
          }
        },
        {
          name: 'dark',
          selectors: ['.dark'],
          mediaQuery: '@media (prefers-color-scheme: dark)',
          theme: {
            colors: {
              dark5: '#10451D',
              dark4: '#155D27',
              dark3: '#1A7431',
              dark2: '#208B3A',
              dark1: '#25A244',
              light1: '#2DC653',
              light2: '#4AD66D',
              light3: '#6EDE8A',
              light4: '#92E6A7',
              light5: '#B7EFC5'
            }
          }
        }
      ]
    }),
    require('@tailwindcss/forms')
  ]
}
