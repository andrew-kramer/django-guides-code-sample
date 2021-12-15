/**
 * NOTE: Webpack isn't actually configured using this file; it mainly uses vue.config.js. However, this config file will
 * trick some IDEs into handling webpack aliases properly.
 */

const path = require('path')

module.exports = {
    entry: {
        app: ['./src/main.ts']
    },
    resolve: {
        alias: {
            '@': path.resolve(__dirname, './src')
        }
    }
}
