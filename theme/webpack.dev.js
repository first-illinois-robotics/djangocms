const Path = require("path");
const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = merge(common, {
    target: "web",
    mode: 'development',
    devtool: "inline-cheap-source-map",
    devServer: {
        contentBase: './dist',
    },
    plugins: [
        new MiniCssExtractPlugin({ filename: "css/[name].css" }),
    ],
    module: {
        rules: [
            {
                test: /\.ts$/,
                exclude: /node_modules/,
                use: "ts-loader",
            },
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
