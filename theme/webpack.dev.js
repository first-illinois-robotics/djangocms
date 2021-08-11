const Path = require("path");
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
    plugins: [
        new MiniCssExtractPlugin({ filename: "css/[name].css" }),
        new HtmlWebpackPlugin({
            template: path.resolve(__dirname, './asset-tags.ejs'),
            filename: path.resolve(__dirname, '../firweb/templates/generated/asset-tags.html'),
            inject:false,
        }),
        new HtmlWebpackPluginDjango({ bundlePath: "" }),
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
