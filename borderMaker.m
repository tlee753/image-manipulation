function borderMaker ()
% function to create  pixel border around an image
% works with .jpg's and .png's (including png transparency)

imageFile = input('File name? (In same directory)\n', 's');
borderSize = input('Border size? (Specify a number of pixels)\n');

[img, ~, alpha] = imread(imageFile);

layer = img(:, :, 1);
[rows, cols] = size(layer);

vertArray = 255 * ones(borderSize, cols);
vertBorder = cat(3, vertArray, vertArray, vertArray);
img = [vertBorder; img; vertBorder];

horzArray = 255 * ones(rows + 2*borderSize, borderSize);
horzBorder = cat(3, horzArray, horzArray, horzArray);
img = [horzBorder, img, horzBorder];

if (strcmp(imageFile(end-3:end), '.jpg'))
    newImageName = [imageFile(1:end-4), '_border.jpg'];
    imwrite(img, newImageName);
    
elseif (strcmp(imageFile(end-3:end), '.png'))
    alphaVertArray = zeros(borderSize, cols);
    alpha = [alphaVertArray; alpha; alphaVertArray];
    alphaHorzArray = zeros(rows + 2*borderSize, borderSize);
    alpha = [alphaHorzArray, alpha, alphaHorzArray];

    newImageName = [imageFile(1:end-4), '_border.png'];
    imwrite(img, newImageName, 'Alpha', alpha);
    
end