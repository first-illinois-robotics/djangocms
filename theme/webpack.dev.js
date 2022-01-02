const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const path = require("path");
const HtmlWebpackPluginDjango = require("html-webpack-plugin-django");

module.exports = merge(common, {
    target: "web",
    mode: 'development',
    devtool: "inline-cheap-source-map",
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
