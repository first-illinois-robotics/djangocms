const path = require('path');
const {CleanWebpackPlugin} = require("clean-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");
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
        new MiniCssExtractPlugin({
            filename: "css/[name].[contenthash].css",
        }),
        new HtmlWebpackPlugin({
            template: path.resolve(__dirname, './asset-tags.ejs'),
            filename: path.resolve(__dirname, '../firweb/templates/generated/asset-tags.html'),
            cache: false,
            inject:false,
            alwaysWriteToDisk: true,
        }),
        new HtmlWebpackPluginDjango({ bundlePath: "" }),
        new CleanWebpackPlugin(),
    ],
    module: {
        rules: [
            {
                test: /\.ts$/,
                exclude: /node_modules/,
                use: "ts-loader",
            },
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

