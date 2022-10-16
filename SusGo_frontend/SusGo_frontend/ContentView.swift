//
//  ContentView.swift
//  SusGo_frontend
//
//  Created by Lily Pham on 10/14/22.
//
import SwiftUI

struct ContentView: View {

    var body: some View {
        ZStack{
            Image("background").resizable().frame(maxWidth: .infinity, maxHeight: .infinity).scaledToFill()
                .background(.black)
            
            VStack{
                
                // Logo Image
                Image("logo").resizable().padding(3.0).frame(width: 200, height: 100).scaledToFit().offset(x: 0.0, y: -75.0)
                
                
                //Button for Sign in
                Button(action: {/** What the button should do**/}, label: {Image("signbubble").resizable().padding(3.0).frame(width: 200, height: 50).scaledToFit().offset(x: 0.0, y: -25.0)})
                
                ZStack{
                Text("Sign In")
                    .font(.headline)
                    .foregroundColor(Color.white).offset(x: 0.0, y: -70.0)
                }
                
                //Button for Sign up
                Button(action: {/** What the button should do**/}, label: {Image("signbubble").resizable().padding(3.0).frame(width: 200, height: 50).scaledToFit().offset(x: 0.0, y: -35.0)})
                
                
                ZStack{
                Text("Sign Up")
                    .font(.headline)
                    .foregroundColor(Color.white).offset(x: 0.0, y: -80.0)
                }
            }
            
        }

    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
