const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');
const CompressionPlugin = require("compression-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const FaviconsWebpackPlugin = require('favicons-webpack-plugin');
const path = require("path");

module.exports = merge(common, {
    mode: 'production',
    devtool: "source-map",
    bail: true,
    output: {
        filename: "js/[name].[chunkhash:8].js",
        chunkFilename: "js/[name].[chunkhash:8].chunk.js",
        publicPath: "/static/"
    },
    plugins: [
        new FaviconsWebpackPlugin({
            logo: './vertical-4c.png',
            publicPath: '/', // it'll read from this variable twice for some reason, so we're appending static to the prefix instead
            outputPath: './assets/',
            prefix: 'static/assets/',
        }),
        new CompressionPlugin()
    ],
    module: {
        rules: [
            {
                test: /\.s?css/i,
                use: [
                    MiniCssExtractPlugin.loader,
                    "css-loader",
                    "postcss-loader",
                    "sass-loader",
                ],
            },
        ],
    },
});
