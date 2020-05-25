module.exports = (req, _, next) => {
    dataset = req.body
    last_y_x = dataset[dataset.length - 1].y[0][0]

    switch (last_y_x) {
        case 182.67929:
            req.url = '/multiple'
            break
        case 972.22461:
        case 972.2246:
            req.url = '/sequence'
            break
    }

    req.originalUrl = req.url
    req._parsedUrl.pathname = req.url
    req._parsedUrl.path = req.url
    req._parsedUrl.href = req.url
    req._parsedUrl._raw = req.url
    req.method = 'GET'

    next()
}
