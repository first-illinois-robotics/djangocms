const path = require('path');
const {CleanWebpackPlugin} = require("clean-webpack-plugin");
const HtmlWebpackPlugin = require('html-webpack-plugin');
const HtmlWebpackPluginDjango = require("html-webpack-plugin-django");

module.exports = {
    entry: {
        'main': './ts/index.ts'
    },
    output: {
        path: path.resolve('./dist/'),
        filename: "[name]-[chunkhash].js",
        chunkFilename: "[name]-[chunkhash].js",
    },
    optimization: {
        splitChunks: {
            chunks: "all",
        },
        runtimeChunk: "single",
    },
    plugins: [
        new CleanWebpackPlugin(),
    ],
    module: {
        rules: [
            {
                test: /\.mjs$/,
                include: /node_modules/,
                type: "javascript/auto",
            },
            {
                test: /\.(ico|jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2)(\?.*)?$/,
                use: {
                    loader: "file-loader",
                    options: {
                        name: "[path][name].[ext]",
                    },
                },
            },
        ],
    },
};

