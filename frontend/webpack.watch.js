const { merge } = require('webpack-merge');
const dev = require('./webpack.dev.js');
const HtmlWebpackHarddiskPlugin = require('html-webpack-harddisk-plugin');
const path = require("path");

module.exports = merge(dev, {
    output: {
        publicPath: "http://localhost:9001/"
    },
    devServer: {
        publicPath: "/",
        contentBase: path.join(__dirname, 'dist'),
        port: 9001,
        writeToDisk: true,
    },
    plugins: [
        new HtmlWebpackHarddiskPlugin()
    ],
});
