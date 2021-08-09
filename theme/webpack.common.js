const path = require('path');
const {CleanWebpackPlugin} = require("clean-webpack-plugin");
const CopyWebpackPlugin = require("copy-webpack-plugin");
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    entry: {
        'main': './ts/index.ts'
    },
    output: {
        path: path.resolve('./dist/'),
        filename: "[name]-[hash].js",
        chunkFilename: "[name]-[hash].js",
        publicPath: "static/"
    },
    optimization: {
        splitChunks: {
            chunks: "all",
        },

        runtimeChunk: "single",
    },
    plugins: [
        new CleanWebpackPlugin(),
        new HtmlWebpackPlugin({
            template: path.resolve(__dirname, './frontend_base.ejs'),
            filename: path.resolve(__dirname, '../firweb/templates/generated/frontend-base.html'),
            inject:false,
        }),
    ],
    resolve: {
        alias: {
            "~": path.resolve(__dirname, "../src"),
        },
    },
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

