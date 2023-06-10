import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import 'intersection-observer';
import { removeDuplicates } from '../src/services/utils';
import ImageComponent from "../src/components/ImageComponent";

describe('imagesComponent', () => {
    it('renders correctly', async () => {
        render(<ImageComponent image={["https://api.slingacademy.com/public/sample-photos/10.jpeg", "Yard"]} />);
        const imagen = await screen.findByAltText('Yard'); // Añade await aquí

        await expect(imagen).toBeInTheDocument();
    });
    it("image  not loaded ", async ()=>{
        render(<ImageComponent image={["https://api.slingacademy.com/public/sample-photos/sad.jpeg", "not loaded"]} />);
        const imagen = await screen.findByAltText('not loaded');

        expect(imagen).toHaveAttribute('src', '');
    })
});


describe('removeDuplicates', () => {
    it('Remove Duplicates', () => {
        const param:[string,string][] = [
            ["aaa","aaa"],
            ["bbb","bbb"],
            ["aaa","aaa"],
        ]
        const expected:[string,string][] = [
            ["aaa","aaa"],
            ["bbb","bbb"],
        ]
        const data = removeDuplicates(param)
        expect(data).toStrictEqual(expected)
    });
});

