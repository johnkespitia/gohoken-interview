import { getServerSideProps } from '@/services/client';

describe('getServerSideProps', () => {
    beforeEach(() => {
        jest.resetModules();
        jest.restoreAllMocks();
    });

    test('returns data when fetch is successful', async () => {
        const mockData = [{ id: 1, name: 'Image 1' }, { id: 2, name: 'Image 2' }];

        global.fetch = jest.fn().mockResolvedValueOnce({
            json: jest.fn().mockResolvedValueOnce(mockData),
        });

        const result = await getServerSideProps();

        expect(global.fetch).toHaveBeenCalledTimes(1);
        expect(global.fetch).toHaveBeenCalledWith(`${process.env.API_URL}/images`);

        expect(result).toEqual({
            props: {
                data: mockData,
            },
        });
    });

    test('returns null data when fetch fails', async () => {
        global.fetch = jest.fn().mockRejectedValueOnce(new Error('Fetch error'));

        const result = await getServerSideProps();

        expect(global.fetch).toHaveBeenCalledTimes(1);
        expect(global.fetch).toHaveBeenCalledWith(`${process.env.API_URL}/images`);

        expect(result).toEqual({
            props: {
                data: null,
            },
        });
    });
});