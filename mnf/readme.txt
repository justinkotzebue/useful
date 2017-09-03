mnf(signal, noise)
    Computes Minimum Noise Fraction / Noise-Adjusted Principal Components.

    Arguments:

        `signal` (:class:`~spectral.algorithms.algorithms.GaussianStats`):

            Estimated signal statistics

        `noise` (:class:`~spectral.algorithms.algorithms.GaussianStats`):

            Estimated noise statistics

    Returns an :class:`~spectral.algorithms.algorithms.MNFResult` object,
    containing the Noise-Adjusted Principal Components (NAPC) and methods for
    denoising or reducing dimensionality of associated data.

    The Minimum Noise Fraction (MNF) is similar to the Principal Components
    transformation with the difference that the Principal Components associated
    with the MNF are ordered by descending signal-to-noise ratio (SNR) rather
    than overall image variance. Note that the eigenvalues of the NAPC are
    equal to one plus the SNR in the transformed space (since noise has
    whitened unit variance in the NAPC coordinate space).

    Example:

        >>> data = open_image('92AV3C.lan').load()
        >>> signal = calc_stats(data)
        >>> noise = noise_from_diffs(data[117: 137, 85: 122, :])
        >>> mnfr = mnf(signal, noise)

        >>> # De-noise the data by eliminating NAPC components where SNR < 10.
        >>> # The de-noised data will be in the original coordinate space (at
        >>> # full dimensionality).
        >>> denoised = mnfr.denoise(snr=10)

        >>> # Reduce dimensionality, retaining NAPC components where SNR >= 10.
        >>> reduced = mnfr.reduce(snr=10)

        >>> # Reduce dimensionality, retaining top 50 NAPC components.
        >>> reduced = mnfr.reduce(num=50)
