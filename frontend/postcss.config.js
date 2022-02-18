module.exports = {
  plugins: [
    require('cssnano')({
        preset: 'default',
        plugins: [require('autoprefixer')]
    }),
  ]
}