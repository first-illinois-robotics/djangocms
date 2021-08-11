const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const HtmlWebpackHarddiskPlugin = require('html-webpack-harddisk-plugin');
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
        new MiniCssExtractPlugin({ filename: "css/[name].css" }),
        new HtmlWebpackPlugin({
            template: path.resolve(__dirname, './asset-tags.ejs'),
            filename: path.resolve(__dirname, '../firweb/templates/generated/asset-tags.html'),
            cache: false,
            inject:false,
            alwaysWriteToDisk: true
        }),
        new HtmlWebpackHarddiskPlugin()
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
