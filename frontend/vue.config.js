// noinspection MagicNumberJS
const BundleTracker = require('webpack-bundle-tracker')

/**
 * @type {import('@vue/cli-service').ProjectOptions}
 */
module.exports = {
  css: {
    loaderOptions: {
      sass: {
        implementation: require('sass')
      }
    },
    sourceMap: true
  },
  chainWebpack: (config) => {
    config
      .plugin('BundleTracker')
      .use(BundleTracker, [{ filename: './dist/webpack-stats.json' }])

    config.output.filename('js/bundle.js')

    config.optimization.splitChunks(false)

    config.resolve.alias.set('__STATIC__', 'static')

    config.devServer
      .public('http://localhost')
      .host('frontend')
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .disableHostCheck(true)
      .headers({ 'Access-Control-Allow-Origin': '*' })
  },
  pages: {
    index: {
      entry: 'src/main.ts',
      title: process.env.SITE_NAME ?? 'Django Guides Code Sample'
    }
  }
}
