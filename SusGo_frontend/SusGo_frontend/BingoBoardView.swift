//
//  BingoBoardView.swift
//  SusGo_frontend
//
//  Created by Lily Pham on 10/15/22.
//

import SwiftUI

struct BingoBoardView: View {
    var body: some View {
        
        ZStack {
            Color.black.ignoresSafeArea()
            VStack {
                Text("10/16 - 10/23")
                    .font(.largeTitle)
                    .foregroundColor(Color.white).offset(x: 0.0, y: -100.0)
                
                Image("logo").resizable().padding(3.0).frame(width: 200, height: 80).scaledToFit().offset(x: 0.0, y: -75.0).offset(x: -80, y: -225)
                Image("profile").resizable().frame(width: 80, height: 80).clipShape(Circle()).overlay(Circle().stroke(Color.white, lineWidth: 2)).offset(x: 140, y: -385)
            
            }
            
            ScrollView(.vertical, showsIndicators: false) {
                ForEach(0..<CollectionViewCell.row) { i in
                    HStack {
                        ForEach(0..<CollectionViewCell.column) { j in CollectionViewCell().onTapGesture {
                            let index = i+j+(i*2)
                            print("\(i),\(j)")
                        }
                        }
                    }
            }
            
            }
            
            Rectangle()
                .fill(Color(0x98CE9D))
                .frame(maxWidth: .infinity, maxHeight: 100)
                .offset(x: 0, y: 375)
            Button(action: {}, label: {Image("home").resizable().padding(3.0).frame(width: 50, height: 50).scaledToFit().offset(x: -115, y: 368)})
            Button(action: {}, label: {Image("leaderboard").resizable().padding(3.0).frame(width: 50, height: 50).scaledToFit().offset(x: 0, y: 368)})
            Button(action: {}, label: {Image("settings").resizable().padding(3.0).frame(width: 50, height: 50).scaledToFit().offset(x: 115, y: 368)})
        }
    }
}

struct BingoBoardView_Previews: PreviewProvider {
    static var previews: some View {
        BingoBoardView()
    }
}

