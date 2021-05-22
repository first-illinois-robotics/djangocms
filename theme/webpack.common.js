const path = require('path');

module.exports = {
    entry: {
        app: './ts/index.ts',
    },
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, 'dist'),
        clean: true,
    },
};
