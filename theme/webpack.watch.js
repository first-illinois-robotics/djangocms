const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');
const HtmlWebpackHarddiskPlugin = require('html-webpack-harddisk-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const path = require("path");

module.exports = merge(common, {
    target: "web",
    mode: 'development',
    devtool: "inline-cheap-source-map",
    output: {
        publicPath: "http://localhost:9000/"
    },
    devServer: {
        publicPath: "/",
        contentBase: path.join(__dirname, 'dist'),
        port: 9000,
        writeToDisk: true,
    },
    plugins: [
        new HtmlWebpackHarddiskPlugin()
    ],
    module: {
        rules: [
            {
                test: /\.s?css/i,
                use: [
                    MiniCssExtractPlugin.loader,
                    "css-loader",
                    "sass-loader",
                ],
            },
        ],
    },
});
