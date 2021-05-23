const Path = require('path');
const {CleanWebpackPlugin} = require("clean-webpack-plugin");
const CopyWebpackPlugin = require("copy-webpack-plugin");
const WebpackAssetsManifest = require("webpack-assets-manifest");
const BundleTracker = require('webpack-bundle-tracker');


module.exports = {
    entry: {
        'main': './ts/index.ts'
    },
    output: {
        path: path.resolve('./assets/bundles/'),
        filename: "[name]-[hash].js",
        chunkFilename: "[name]-[hash].js"
    },
    optimization: {
        splitChunks: {
            chunks: "all",
        },

        runtimeChunk: "single",
    },
    plugins: [
        new CleanWebpackPlugin(),
        new CopyWebpackPlugin({
            patterns: [
                { from: Path.resolve(__dirname, "./vendors"), to: "vendors" },
            ],
        }),
        new WebpackAssetsManifest({
            entrypoints: true,
            output: "manifest.json",
            writeToDisk: true,
            publicPath: true,
        }),
        new BundleTracker({filename: './webpack-stats.json'})
    ],
    resolve: {
        alias: {
            "~": Path.resolve(__dirname, "../src"),
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

