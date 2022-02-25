const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
var inliner = require('sass-inline-svg');

module.exports = merge(common, {
    target: "web",
    mode: 'development',
    devtool: "inline-cheap-source-map",
    output: {
        publicPath: "/static/"
    },
    module: {
        rules: [
            {
                test: /\.s?css/i,
                use: [
                    MiniCssExtractPlugin.loader,
                    "css-loader",
                    {
                        loader: "sass-loader",
                        options: {
                            sassOptions: {
                                functions: {
                                    "svg($path, $selectors: null)": inliner('./sass')
                                }
                            },
                        },
                    },
                ],
            },
        ],
    },
});
